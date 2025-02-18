import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SuperMACD': 1.0
        })
    )
