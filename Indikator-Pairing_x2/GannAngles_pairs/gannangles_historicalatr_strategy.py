import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'HistoricalATR': 1.0
        })
    )
