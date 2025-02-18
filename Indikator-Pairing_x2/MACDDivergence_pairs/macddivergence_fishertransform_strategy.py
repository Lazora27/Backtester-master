import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FisherTransform
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FisherTransform': 1.0
        })
    )
