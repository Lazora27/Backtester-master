import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
