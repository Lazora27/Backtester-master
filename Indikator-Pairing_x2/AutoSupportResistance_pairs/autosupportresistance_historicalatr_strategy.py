import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HistoricalATR': 1.0
        })
    )
