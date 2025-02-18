import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
