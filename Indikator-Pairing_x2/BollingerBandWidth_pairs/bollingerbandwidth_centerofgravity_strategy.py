import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'CenterOfGravity': 1.0
        })
    )
