import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
