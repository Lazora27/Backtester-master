import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'PhaseDivergence': 1.0
        })
    )
