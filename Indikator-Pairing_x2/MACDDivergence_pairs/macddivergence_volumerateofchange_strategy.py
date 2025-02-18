import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
