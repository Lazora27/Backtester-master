import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
