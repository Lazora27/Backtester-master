import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und Fisher
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'Fisher': 1.0
        })
    )
