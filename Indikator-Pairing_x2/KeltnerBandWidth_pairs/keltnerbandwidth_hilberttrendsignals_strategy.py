import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
