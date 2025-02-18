import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FisherTransform
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FisherTransform': 1.0
        })
    )
