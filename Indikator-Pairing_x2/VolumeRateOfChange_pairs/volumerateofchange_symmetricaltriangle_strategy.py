import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
