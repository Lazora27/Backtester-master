import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TrueRange': 1.0
        })
    )
