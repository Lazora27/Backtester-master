import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
