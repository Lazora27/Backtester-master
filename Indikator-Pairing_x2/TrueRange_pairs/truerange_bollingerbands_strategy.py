import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BollingerBands': 1.0
        })
    )
