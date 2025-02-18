import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
