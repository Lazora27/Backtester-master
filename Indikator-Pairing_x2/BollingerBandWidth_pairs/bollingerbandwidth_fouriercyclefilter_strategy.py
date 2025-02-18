import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
