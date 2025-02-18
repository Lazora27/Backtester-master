import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
