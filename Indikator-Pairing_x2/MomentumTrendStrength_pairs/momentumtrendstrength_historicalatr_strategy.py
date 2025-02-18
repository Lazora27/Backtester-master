import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HistoricalATR': 1.0
        })
    )
