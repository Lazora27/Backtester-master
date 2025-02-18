import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
