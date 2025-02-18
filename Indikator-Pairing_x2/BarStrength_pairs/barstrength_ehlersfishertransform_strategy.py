import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
