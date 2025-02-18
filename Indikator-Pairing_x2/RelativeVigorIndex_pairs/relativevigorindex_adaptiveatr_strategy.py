import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
