import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
