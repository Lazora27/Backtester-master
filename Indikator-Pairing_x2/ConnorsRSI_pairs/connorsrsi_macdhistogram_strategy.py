import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'MACDHistogram': 1.0
        })
    )
