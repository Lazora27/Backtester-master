import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HistoricalATR': 1.0
        })
    )
