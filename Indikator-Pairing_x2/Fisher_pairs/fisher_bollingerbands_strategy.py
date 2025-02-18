import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BollingerBands
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BollingerBands': 1.0
        })
    )
