import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'CenterOfGravity': 1.0
        })
    )
