import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und TrendCycles
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'TrendCycles': 1.0
        })
    )
