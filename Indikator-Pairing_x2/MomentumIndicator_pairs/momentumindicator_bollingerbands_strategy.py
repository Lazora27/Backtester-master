import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
