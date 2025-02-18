import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TrueRange': 1.0
        })
    )
