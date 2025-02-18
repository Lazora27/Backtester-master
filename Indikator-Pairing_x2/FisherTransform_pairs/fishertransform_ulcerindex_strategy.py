import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'UlcerIndex': 1.0
        })
    )
