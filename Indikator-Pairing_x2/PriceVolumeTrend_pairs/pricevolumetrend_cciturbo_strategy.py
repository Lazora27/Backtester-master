import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'CCITurbo': 1.0
        })
    )
