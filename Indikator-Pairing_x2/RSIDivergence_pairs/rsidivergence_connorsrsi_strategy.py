import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ConnorsRSI': 1.0
        })
    )
