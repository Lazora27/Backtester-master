import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
