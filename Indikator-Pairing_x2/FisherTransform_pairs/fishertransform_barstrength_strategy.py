import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BarStrength
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BarStrength': 1.0
        })
    )
