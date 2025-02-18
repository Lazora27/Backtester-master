import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
