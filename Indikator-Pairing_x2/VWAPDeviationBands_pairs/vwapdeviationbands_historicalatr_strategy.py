import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HistoricalATR': 1.0
        })
    )
