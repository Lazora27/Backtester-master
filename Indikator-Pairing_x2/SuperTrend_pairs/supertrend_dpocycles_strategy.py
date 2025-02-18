import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'DPOCycles': 1.0
        })
    )
