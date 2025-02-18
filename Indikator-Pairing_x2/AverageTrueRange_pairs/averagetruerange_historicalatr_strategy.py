import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'HistoricalATR': 1.0
        })
    )
