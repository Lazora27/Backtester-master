import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
