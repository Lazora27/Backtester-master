import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'AccelerationBands': 1.0
        })
    )
