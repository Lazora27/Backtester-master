import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BollingerBands
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BollingerBands': 1.0
        })
    )
