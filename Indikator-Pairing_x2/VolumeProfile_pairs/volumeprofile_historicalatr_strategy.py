import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HistoricalATR': 1.0
        })
    )
