import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und BollingerBands
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'BollingerBands': 1.0
        })
    )
