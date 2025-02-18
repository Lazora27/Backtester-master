import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ModifiedRSI': 1.0
        })
    )
