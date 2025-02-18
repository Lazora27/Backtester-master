import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'PhaseDivergence': 1.0
        })
    )
