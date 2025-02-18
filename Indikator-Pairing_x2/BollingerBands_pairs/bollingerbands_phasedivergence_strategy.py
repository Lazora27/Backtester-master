import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'PhaseDivergence': 1.0
        })
    )
