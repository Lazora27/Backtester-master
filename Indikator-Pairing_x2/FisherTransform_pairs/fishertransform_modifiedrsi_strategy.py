import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ModifiedRSI': 1.0
        })
    )
