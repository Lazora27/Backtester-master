import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedFractalEfficiency_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedFractalEfficiency und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PolarizedFractalEfficiency': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
