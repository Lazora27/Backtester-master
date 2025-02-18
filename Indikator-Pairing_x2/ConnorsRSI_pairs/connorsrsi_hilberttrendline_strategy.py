import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'HilbertTrendline': 1.0
        })
    )
