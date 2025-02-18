import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
