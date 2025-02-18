import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'HistoricalATR': 1.0
        })
    )
